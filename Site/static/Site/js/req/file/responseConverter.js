export const responseConverter = (uploaderFile, response) => {
    response = JSON.parse(response);

    return {
        realId: response.id,
        url: response.data,
        name: response.name,
    }
};