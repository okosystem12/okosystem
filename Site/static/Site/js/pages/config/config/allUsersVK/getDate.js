import {vkInfo} from "../../../../req/config/vkInfo";
import {allUsersVK} from "../../../../storage/config/allUsersVK";
import {update} from "./update";

export const getDate = () => vkInfo((msg) => {
    allUsersVK.value = msg.allUsersVK;

    update()
});