import { reactive } from "vue";
import { Planes } from "./constants";

interface Store {
    plane: string;
    authenticated: boolean;
    tags: string[];
}

export const store = reactive<Store>({
    plane: Planes.CENTER,
    authenticated: false,
    tags: [],
});
