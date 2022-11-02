import {init} from "./table/init";
import {info} from "../../req/archive/info";
import {usersList} from "../../storage/archive/usersList";
import {corruptInfoList} from "../../storage/archive/corruptInfoList";

export const getInfo = () =>
    info((msg) => {
        usersList.value = msg.usersList;
        corruptInfoList.value = msg.corruptInfoList;
        init();
    });

