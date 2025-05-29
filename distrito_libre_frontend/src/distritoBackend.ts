import { getData, postData } from "./apiAccess";
import { APIBASEURL } from "./constants";

export interface DL_QueryParm {
    key: string;
    value: string;
}

export function paramValues(key: string, values: string[]) {
    const qparams: DL_QueryParm[] = [];
    for (const value of values) {
        const param = { key, value };
        qparams.push(param);
    }
    return qparams;
}

export function getPathData<T>(
    path: string,
    queryParms: DL_QueryParm[] = [],
    auth = false,
) {
    path = "/api" + path;
    const url = new URL(path, APIBASEURL);
    for (const val of queryParms) {
        url.searchParams.append(val.key, val.value);
    }
    return getData<T>(url, auth);
}

export function postPathData<RQ extends object, RP>(path: string, data: RQ) {
    const url = new URL(path, APIBASEURL);
    return postData<RQ, RP>(url, data);
}
