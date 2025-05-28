import { ref } from "vue";

export function fetchData<T>(url: RequestInfo | URL, options?: RequestInit) {
    const data = ref<T>();
    const error = ref();
    fetch(url, options)
        .then((resp) => resp.json())
        .then((obj) => (data.value = obj))
        .catch((err) => (error.value = err));
    return { data, error };
}

export function getData<T>(url: RequestInfo | URL, auth = false) {
    let credentials: RequestCredentials = "omit";
    if (auth) credentials = "include";
    return fetchData<T>(url, {
        credentials: credentials,
        method: "GET",
    });
}

export function postData<RQ extends object, RP>(
    url: RequestInfo | URL,
    data: RQ,
) {
    const fdat = new FormData();

    for (const [key, val] of Object.entries(data)) {
        fdat.set(key, val);
    }
    return fetchData<RP>(url, {
        credentials: "include",
        method: "POST",
        body: fdat,
    });
}
