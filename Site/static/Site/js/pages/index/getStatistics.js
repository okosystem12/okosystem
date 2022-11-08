import {get as getControlUser} from "./statistics/controlUser/get";
import {get as getCorrupt} from "./statistics/corrupt/get";
import {get as getArchive} from "./statistics/archive/get";

export const getStatistics = () => {
    getControlUser();
    getCorrupt();
    getArchive();
};