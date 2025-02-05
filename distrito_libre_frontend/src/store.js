import { reactive } from "vue";
import { selectionStage } from "./constants";

export const store = reactive({
    sel_stage: selectionStage.PLANE,
    plane: "",
    section: "",
});
