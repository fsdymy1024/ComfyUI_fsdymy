class IPAdapterLayerWeight:
    def __init__(self):
        self.unfold_batch = False

    @classmethod
    def INPUT_TYPES(cls):
        weights = {
            "layer_00": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.005}),
            "layer_01": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.005}),
            "layer_02": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.005}),
            "layer_03": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.005}),
            "layer_04": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.005}),
            "layer_05": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.005}),
            "layer_06": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.005}),
            "layer_07": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.005}),
            "layer_08": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.005}),
            "layer_09": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.005}),
            "layer_10": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.005}),
        }
        return {
            "required":
                weights
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("ipadapter_layer_weight",)
    FUNCTION = "get_weight"
    CATEGORY = "fsdymy/ipadapter"

    def get_weight(self, layer_00, layer_01, layer_02, layer_03, layer_04, layer_05, layer_06, layer_07, layer_08,
                   layer_09, layer_10):
        text = f"0: {layer_00}, 1: {layer_01}, 2: {layer_02}, 3: {layer_03}, 4: {layer_04}, 5: {layer_05}, 6: {layer_06}, 7: {layer_07}, 8: {layer_08}, 9: {layer_09}, 10: {layer_10}"
        # print(text)
        return (text,)
