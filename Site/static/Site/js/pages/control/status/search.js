import {search as startSearch} from "../../../req/control/status/search";
import {userId} from "../../../storage/control/userId";
import {close} from "../view/close";

export const search = () =>
    startSearch({id: userId.value}, close);