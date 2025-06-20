export const APIBASEURL = "http://localhost:5173/";

export const Planes = {
    CENTER_RIGHT: "CENTER_RIGHT",
    CENTER: "CENTER",
    CENTER_LEFT: "CENTER_LEFT",
};

export const politicalMap = new Map(
    Object.entries({
        CENTER_RIGHT: [
            "ANARQUISMOCRISTIANO",
            "COMUNALISMOTRADICIONALISTA",
            "PAELOLIBERTARISMO",
            "SOCIALISMOCRISTIANO",
            "LIBERALISMOCONSERVADOR",
            "NACIONALBOLCHEVISMO",
            "FASCISMOCLERICAL",
            "NEOREACCIONNRX",
        ],
        CENTER: [
            "ANARCOCOMUNISMO",
            "MUTUALISMO",
            "LIBERTARISMO",
            "SOCIALISMODEMOCRATICO",
            "LIBERALISMOCLASICO",
            "MARXISMOLENINISMO",
            "FASCISMOCLASICO",
            "CAPITALISMOILIBERAL",
        ],
        CENTER_LEFT: [
            "POSANARQUISMO",
            "ANARQUISMOEGOISTA",
            "IZQUIERDALIBERTARIA",
            "LUXEMBURGISMO",
            "SOCIOLIBERALISMO",
            "COMUNISMOPOSMARXISTA",
            "TECNOCRACIAPROGRESISTA",
            "JACOBINISMO",
        ],
    }),
);
