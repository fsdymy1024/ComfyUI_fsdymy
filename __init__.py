from .nodes.imageUtils import SaveImageWithoutMetadata, PreviewImageWithoutMetadata
from .nodes.GLM import ZhiPuAiNode, ShowText

# NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

NODE_CLASS_MAPPINGS = {
    "SaveImageWithoutMetadata": SaveImageWithoutMetadata,
    "PreviewImageWithoutMetadata": PreviewImageWithoutMetadata,
    "ZhiPuAiNode": ZhiPuAiNode,
    "ShowText": ShowText
}
NODE_DISPLAY_NAME_MAPPINGS = {
	"SaveImageWithoutMetadata": "Save Image Without Metadata",
	"PreviewImageWithoutMetadata": "Preview Image Without Metadata",
	"ZhiPuAiNode": "ZhiPu Ai Node",
	"ShowText": "Show Text",
}

WEB_DIRECTORY = "./web"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
