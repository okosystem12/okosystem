const alertList = [
    {type: 'danger', title: 'Ошибка', img: '/static/Site/images/notification/danger.png'},
    {type: 'success', title: 'Выполнено', img: '/static/Site/images/notification/success.png'},
    {type: 'warning', title: 'Внимание', img: '/static/Site/images/notification/warning.png'},
    {type: 'info', title: 'Информирование', img: '/static/Site/images/star.png'},
];

export const showNotification = (type = 'default', text = '', callback) => {

    const _alert = alertList.find(el => el.type === type);

    if (_alert) {
        const notification = new Notification(_alert.title, {
            body: text,
            icon: _alert.img
        });

        if (callback) {
            notification.addEventListener('click', callback)
        }
    }
};