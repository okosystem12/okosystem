import {info as getVchInfo} from "../../req/config/vch/info";

export const vchInfo = () =>
    getVchInfo((msg) => {
        console.log(msg);
    });