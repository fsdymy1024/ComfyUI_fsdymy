class IPAdapterLayerWeight:
    def __init__(self):
        self.unfold_batch = False

    @classmethod
    def INPUT_TYPES(cls):
        weights = {
            "index_00": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 5.0, "step": 0.1}),
            "index_01": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 5.0, "step": 0.1}),
            "index_02": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 5.0, "step": 0.1}),
            "index_03": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 5.0, "step": 0.1}),
            "index_04": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 5.0, "step": 0.1}),
            "index_05": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 5.0, "step": 0.1}),
            "index_06": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 5.0, "step": 0.1}),
            "index_07": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 5.0, "step": 0.1}),
            "index_08": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 5.0, "step": 0.1}),
            "index_09": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 5.0, "step": 0.1}),
            "index_10": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 5.0, "step": 0.1}),
            "index_11": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 5.0, "step": 0.1}),
        }
        return {
            "required":
                weights
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("ipadapter_layer_weight",)
    FUNCTION = "get_weight"
    CATEGORY = "fsdymy/ipadapter"

    def get_weight(self, index_00, index_01, index_02, index_03, index_04, index_05, index_06, index_07, index_08, index_09, index_10, index_11):
        text = f"{index_00},{index_01},{index_02},{index_03},{index_04},{index_05},{index_06},{index_07},{index_08},{index_09},{index_10},{index_11}"
        # print(text)
        return (text,)
