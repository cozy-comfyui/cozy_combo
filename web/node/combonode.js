/**/

import { app } from "../../../scripts/app.js"

const _ID = "ComboNodeCozy";

app.registerExtension({
	name: 'cozy_comfy.' + _ID,
	async beforeRegisterNodeDef(nodeType, nodeData, app) {
        // skip the node if it is not the one we want
        if (nodeData.name !== _ID) {
            return
        }

        const onNodeCreated = nodeType.prototype.onNodeCreated;
        nodeType.prototype.onNodeCreated = async function () {
            const me = onNodeCreated?.apply(this);
            const combo = this.widgets.find(w => w.name == 'combo');
            const text = this.widgets.find(w => w.name == 'text');
            combo.callback = () => {
                if (combo.value == "SOME") {
                    text.value = "Where it is nobler for some to suffer slings and arrows"
                } else if (combo.value == "OTHER") {
                    text.value = "Or others to take the burden of writing example code for ComfyUI"
                } else {
                    text.value = "Snarf says: BLARF, BLARF, BLARF."
                }
            }
            return me;
        }
        return nodeType;
    },
})
