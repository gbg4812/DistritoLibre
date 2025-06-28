export function isString(data: unknown): data is string {
    return typeof data === "string";
}

export function isNumber(data: unknown): data is number {
    return typeof data === "number";
}

export function isElement(data: unknown): data is HTMLElement {
    return data instanceof HTMLElement;
}
