import {show} from "../../../utils/modal/show";
import {componentsData} from "../componentsData";
import {setViewValue} from "./setViewValue";
import {userId} from "../../../storage/control/userId";

export const openView = (data = {}) =>
    show(
        componentsData.viewModal,
        () => setViewValue(data),
        () => {
            userId.clear();
        }
    );