import { reactive } from "vue";
import { Planes } from "./constants";

export const store = reactive({
    plane: Planes.CENTER,
    authenticated: false,
    tags: [],
});
