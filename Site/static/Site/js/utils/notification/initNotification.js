export const initNotification = () => {
    if (!('Notification' in window)) {
        console.log("This browser does not support notifications.");
    }
    else {
        (async () => {
            if (Notification.permission !== 'granted' && Notification.permission !== 'denied') {
                await Notification.requestPermission();
            }
        })();
    }
};