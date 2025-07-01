export const APIBASEURL = "http://localhost:5173/";

export enum Planes {
    CENTER_RIGHT = "CENTER_RIGHT",
    CENTER = "CENTER",
    CENTER_LEFT = "CENTER_LEFT",
    NONE = "NONE",
}

export const buildings = [
    "Hospital",
    "Library",
    "Police Station",
    "Fire Station",
    "City Hall",
    "Post Office",
    "School",
    "University",
    "Museum",
    "Theater",
    "Courthouse",
    "Train Station",
    "Bus Terminal",
    "Airport",
    "Community Center",
    "Sports Arena",
    "Shopping Mall",
    "Public Market",
    "Power Plant",
    "Water Treatment Plant",
];
export const politicalMap = {
    CENTER_RIGHT: [
        "ANARQUISMO_CRISTIANO",
        "COMUNALISMO_TRADICIONALISTA",
        "PAELO_LIBERTARISMO",
        "SOCIALISMO_CRISTIANO",
        "LIBERALISMO_CONSERVADOR",
        "NACIONAL_BOLCHEVISMO",
        "FASCISMO_CLERICAL",
        "NEO_REACCIONNRX",
    ],
    CENTER: [
        "ANARCO_COMUNISMO",
        "MUTUALISMO",
        "LIBERTARISMO",
        "SOCIALISMO_DEMOCRATICO",
        "LIBERALISMO_CLASICO",
        "MARXISMO_LENINISMO",
        "FASCISMO_CLASICO",
        "CAPITALISMO_LIBERAL",
    ],
    CENTER_LEFT: [
        "POS_ANARQUISMO",
        "ANARQUISMO_EGOISTA",
        "IZQUIERDA_LIBERTARIA",
        "LUXEMBURGISMO",
        "SOCIO_LIBERALISMO",
        "COMUNISMO_POSMARXISTA",
        "TECNOCRACIA_PROGRESISTA",
        "JACOBINISMO",
    ],
};
