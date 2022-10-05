export const parseSearch = () => {
    const result = [];

    window.location.search.substr(1).split('&').forEach(el => {
        const item = el.split('=');
        result.push({
            key: item[0] || '',
            value: item[1] || ''
        })
    });

    return result.filter(el => el !== '');
};