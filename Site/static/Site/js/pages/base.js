import {initNotification} from "../utils/notification/initNotification";
import {validator} from "../utils/form/validator";
import {userInfo} from "./base/userInfo";


(()=>{
    initNotification();
    validator();

    userInfo();
})();