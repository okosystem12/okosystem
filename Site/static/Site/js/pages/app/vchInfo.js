import {info as getVchInfo} from "../../req/config/vch/info";
import {init} from "../config/vch/table/init";
import {vchList} from "../../storage/app/vchList";

export const vchInfo = () =>
    getVchInfo((msg) => {
        vchList.value = msg.vchList;
        console.log(msg);
        init();
    });