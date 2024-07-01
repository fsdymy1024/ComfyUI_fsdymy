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
        text = f"0: {index_00}, 1: {index_01}, 2: {index_02}, 3: {index_03}, 4: {index_04}, 5: {index_05}, 6: {index_06}, 7: {index_07}, 8: {index_08}, 9: {index_09}, 10: {index_10}, 11: {index_11}"
        return (text,)
