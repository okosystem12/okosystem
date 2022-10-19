import {componentsData} from "../../componentsData";
import {redirect} from "../../../../utils/redirect";
import {userId} from "../../../../storage/control/userId";

export const btnViewArchiveEvent = () =>
    componentsData.viewArchiveBtn.on('click', (e) => redirect(`${e.currentTarget.dataset.href}?id=${userId.value}`));