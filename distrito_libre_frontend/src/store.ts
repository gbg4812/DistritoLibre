import { reactive } from "vue";
import { Planes } from "./constants";
import type { UserInfo } from "./types";

interface Store {
    plane: string;
    user?: UserInfo;
    tags: string[];
}

export const store = reactive<Store>({
    plane: Planes.CENTER,
    tags: [],
});
