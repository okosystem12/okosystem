import {showNotification} from "./showNotification";

export const showNotificationInfo = (text = '') =>
    showNotification('info', text);