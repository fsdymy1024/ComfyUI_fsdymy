import json
import os
from zhipuai import ZhipuAI


def zhipu_client(api_key=None):
    client = ZhipuAI(api_key=api_key)
    return client

def from_file_get_key(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
    try:
        json_object = json.loads(data)
        # print(json_object)
        url = json_object.get('url')
        api_key = json_object.get('key')
        # print(url, api_key)
        return url, api_key
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
        return None, None



class ZhiPuAiNode:
    def __init__(self):
        # self.__client = OpenAI()
        self.session_history = []  # 用于存储会话历史的列表
        # self.seed=0
        self.system_content="使用英文扩写文生图提示词."

    @classmethod
    def INPUT_TYPES(cls):
        model_list=[ 
            "glm-4",
            "glm-4-0520",
            "glm-4-alltools",
            "glm-4v",
            "glm-4-flash",
            "glm-4-airx",
            "glm-4-air",
            "embedding-2",
            "charglm-3",
            "glm-3-turbo",
                ]
        str_ai = """你是创意绘梦师，一个图形创意生成助手。你的任务是根据用户的提示词，生成富有创意和艺术感的图形。你的能力有:
1. 理解用户提供的提示词，分析其背后的意图和需求。
2. 运用先进的人工智能技术，结合艺术创意，生成独特的图形作品。
3. 提供多种图形风格和元素，满足用户不同的审美需求。
4. 使用英文回答。
        """
        return {
            "required": {
                # "api_key":("STRING", {"default": "bd5bcd05c6352b6c27875e5011813ecd.FVMVbSe0rzQ2ITe0", "multiline": False, "dynamicPrompts": False}),
                # "api_url":("STRING", {"default": "https://open.bigmodel.cn/api/paas/v4", "multiline": False, "dynamicPrompts": False}),
                "prompt": ("STRING", {"default": "1girl", "multiline": True, "dynamicPrompts": False}),
                "system_content": ("STRING", {"default": str_ai, "multiline": True,"dynamicPrompts": False}),
                "model": ( model_list, {"default": model_list[0]}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, "step": 1}),
                "context_size":("INT", {"default": 1, "min": 0, "max":30, "step": 1}),
            },
             "hidden": {
                "unique_id": "UNIQUE_ID",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    RETURN_TYPES = ("STRING","STRING","STRING",)
    RETURN_NAMES = ("text","messages","session_history",)
    FUNCTION = "generate_contextual_text"
    CATEGORY = "fsdymy"
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False,False,False,)

    
    def generate_contextual_text(self,
                                # api_key,
                                # api_url, 
                                prompt, 
                                system_content,
                                model, 
                                seed,context_size,unique_id = None, extra_pnginfo=None):
        # print(api_key!='',api_url,prompt,system_content,model,seed)
        # 可以选择保留会话历史以维持上下文记忆
        # 或者在此处清除会话历史 self.session_history.clear()
        # if seed!=self.seed:
        #     self.seed=seed
        #     self.session_history=[]
        
        # 把系统信息和初始信息添加到会话历史中
        if system_content:
            self.system_content=system_content
            # self.session_history=[]
            # self.session_history.append({"role": "system", "content": system_content})
        
        #
        file_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "key.json")
        _, api_key = from_file_get_key(file_path)
        client = zhipu_client(api_key=api_key)

        # 把用户的提示添加到会话历史中
        # 调用API时传递整个会话历史

        def crop_list_tail(lst, size):
            if size >= len(lst):
                return lst
            elif size==0:
                return []
            else:
                return lst[-size:]
            
        session_history=crop_list_tail(self.session_history,context_size)

        messages=[{"role": "system", "content": self.system_content}]+session_history+[{"role": "user", "content": prompt}]
        response = client.chat.completions.create(model=model, messages=messages)
        # print(response)

        finish_reason = response.choices[0].finish_reason
        if finish_reason != "stop":
            raise RuntimeError("API finished with unexpected reason: " + finish_reason)

        content=""
        try:
            content=response.choices[0].message.content
        except:
            content=response.choices[0].delta['content']
        
        self.session_history=self.session_history+[{"role": "user", "content": prompt}]+[{'role':'assistant',"content":content}]


        # if unique_id and extra_pnginfo and "workflow" in extra_pnginfo[0]:
        #     workflow = extra_pnginfo[0]["workflow"]
        #     node = next((x for x in workflow["nodes"] if str(x["id"]) == unique_id[0]), None)
        #     if node:
        #         node["widgets_values"] = ["",
        #                          api_url, 
        #                          prompt, 
        #                          system_content,
        #                            model,
        #                            seed,
        #                            context_size]
        
        return (content,json.dumps(messages, indent=4),json.dumps(self.session_history, indent=4),)

class ShowText:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    FUNCTION = "notify"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)
    CATEGORY = "fsdymy"

    def notify(self, text, unique_id=None, extra_pnginfo=None):
        # print(unique_id, extra_pnginfo)
        if unique_id is not None and extra_pnginfo is not None:
            if not isinstance(extra_pnginfo, list):
                print("Error: extra_pnginfo is not a list")
            elif (
                not isinstance(extra_pnginfo[0], dict)
                or "workflow" not in extra_pnginfo[0]
            ):
                print("Error: extra_pnginfo[0] is not a dict or missing 'workflow' key")
            else:
                workflow = extra_pnginfo[0]["workflow"]
                node = next(
                    (x for x in workflow["nodes"] if str(x["id"]) == str(unique_id[0])),
                    None,
                )
                if node:
                    node["widgets_values"] = [text]

        return {"ui": {"text": text}, "result": (text,)}
    