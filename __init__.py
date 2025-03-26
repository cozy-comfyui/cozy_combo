"""
@title: cozy_combo
@author: amorano
@category: Example
@reference: https://github.com/cozy-comfyui/cozy_combo
@tags: dynamic, example, developer, script, mechanism, exemplar
@description: Example of a Combo widget changing Node appearance
@node list:
    ComboNodeCozy
@version: 1.0.0
"""

# =============================================================================
# === GLOBAL ===
# =============================================================================

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]

# =============================================================================
# === NODE ===
# =============================================================================

class ComboNodeCozy:
    """
    A class to represent a dynamic combo changer in ComfyUI.
    """
    RETURN_TYPES = ()
    RETURN_NAMES = ()
    CATEGORY = "_EXAMPLES"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {},
            "optional": {
                "combo": (["NONE", "SOME", "OTHER"], {"default": "NONE"}),
                "text": ("STRING", {"default": "BLARF", "multiline": True})
            }
        }

# =============================================================================
# === REGISTRATION ===
# =============================================================================

NODE_CLASS_MAPPINGS = {
    "ComboNodeCozy": ComboNodeCozy,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComboNodeCozy": "Combo Node (cozy)",
}
