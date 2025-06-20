import { APIBASEURL } from "./constants";
import { createFetch } from "@vueuse/core";
import type { Post, PostOverview, StateResponse } from "./types";

export type SearchParams = Map<string, string | string[]>;

export function isString(data: string | string[]): data is string {
    return typeof data === "string";
}

export function toFormData(data: object): FormData {
    const res = new FormData();
    for (const [key, value] of Object.entries(data)) {
        res.set(key, value);
    }
    return res;
}

export const useDistritoFetch = createFetch({
    baseUrl: APIBASEURL,
    fetchOptions: {
        credentials: "include",
    },
});

export function apiUrl(path: string) {
    if (!path.endsWith("/")) throw Error(`Path ${path} has to end with /`);
    if (!path.startsWith("/")) throw Error(`Path ${path} has to start with /`);
    const url = new URL("/api" + path, APIBASEURL);
    return url;
}

export async function getPost(id: number) {
    const url = apiUrl(`/posts/detail/${id}/`);
    const rawdata = await fetch(url, { method: "GET" });
    const data = (await rawdata.json()) as Post;
    return data;
}

export async function postPost(post: Post) {
    const url = apiUrl("/posts/new/");
    const data = toFormData(post);
    const raw = await fetch(url, {
        method: "POST",
        credentials: "include",
        body: data,
    });
    const response = (await raw.json()) as StateResponse;

    return response;
}

export async function getPostList(params?: SearchParams) {
    const url = apiUrl(`/posts/`);
    if (params) {
        for (const [key, value] of params.entries()) {
            if (isString(value)) {
                url.searchParams.set(key, value);
            } else {
                for (const val of value) {
                    url.searchParams.append(key, val);
                }
            }
        }
    }
    const rawdata = await fetch(url, { method: "GET" });
    const data = (await rawdata.json()) as PostOverview[];
    return data;
}
