export const bDate = (user) => {
    if (user.birthDay === 0 || user.birthMonth === 0 || user.birthYear === 0) {
        return '';
    }
    return new Date(user.birthYear, user.birthMonth - 1, user.birthDay);
};