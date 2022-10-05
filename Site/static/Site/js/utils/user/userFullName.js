export const userFullName = (user) =>
    [
        user['lastName'],
        user['firstName'],
        user['patronymic']
    ].filter(el => el).join(' ');