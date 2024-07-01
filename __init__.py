from .nodes.GLM import ZhiPuAiNode, ShowText
from .nodes.IPAdapterLayerWeight import IPAdapterLayerWeight
from .nodes.imageUtils import SaveImageWithoutMetadata, PreviewImageWithoutMetadata

NODE_CLASS_MAPPINGS = {
    "SaveImageWithoutMetadata": SaveImageWithoutMetadata,
    "PreviewImageWithoutMetadata": PreviewImageWithoutMetadata,
    "ZhiPuAiNode": ZhiPuAiNode,
    "ShowText": ShowText,
    "IPAdapterLayerWeight": IPAdapterLayerWeight,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "SaveImageWithoutMetadata": "Save Image Without Metadata (fsdymy)",
    "PreviewImageWithoutMetadata": "Preview Image Without Metadata (fsdymy)",
    "ZhiPuAiNode": "ZhiPu Ai Node (fsdymy)",
    "ShowText": "Show Text (fsdymy)",
    "IPAdapterLayerWeight": "IPAdapter Layer Weight (fsdymy)",
}

WEB_DIRECTORY = "./web"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
