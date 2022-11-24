import {init as initAllUsersVK} from "./config/allUsersVK/init";
import {init as initToken} from "./config/token/init";

(() => {
    initAllUsersVK();
    initToken();
})();