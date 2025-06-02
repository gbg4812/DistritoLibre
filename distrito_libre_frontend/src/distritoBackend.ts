import { APIBASEURL } from "./constants";
import { createFetch } from "@vueuse/core";

export const useDistritoFetch = createFetch({
    baseUrl: APIBASEURL,
    fetchOptions: {
        credentials: "include",
    },
});
