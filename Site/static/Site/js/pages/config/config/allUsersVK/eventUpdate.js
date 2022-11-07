import {componentsData} from "../componentsData";
import {vkUpdate} from "../../../../req/config/vkUpdate";
import {getDate} from "./getDate";

export const eventUpdate = () =>
    componentsData.updateAllUsersVK.click(() => vkUpdate(() => {
        getDate();
    }));