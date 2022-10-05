export const userShortName = (user) =>
    [
        user['lastName'],
        [
            user['firstName'] ? (user['firstName'][0] + '.')  : '',
            user['patronymic'] ? (user['patronymic'][0] + '.')  : '',
        ].filter(el => el).join('')
    ].filter(el => el).join(' ');