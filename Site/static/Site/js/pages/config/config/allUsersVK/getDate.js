import {vkInfo} from "../../../../req/config/vkInfo";
import {update} from "./update";

export const getDate = () =>
    vkInfo((msg) =>
        update(msg.allUsersVK));