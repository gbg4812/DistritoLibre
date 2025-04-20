import { reactive } from "vue";
import { selectionStage, Planes } from "./constants";

export const store = reactive({
    sel_stage: selectionStage.PLANE,
    plane: Planes.CENTER,
    tags: [],
});
