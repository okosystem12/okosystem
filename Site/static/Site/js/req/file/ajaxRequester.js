export const ajaxRequester = (config, uploaderFile, progressCallback, successCallback, errorCallback) => {
    $.ajax({
        url: config.url,
        contentType: false,
        processData: false,
        method: config.method,
        data: config.paramsBuilder(uploaderFile),
        success: (response) => {
            successCallback(response);
        },
        error: (response) => {
            console.error("Error", response);
            errorCallback("Error");
        },
        xhr: () => {
            let xhr = new XMLHttpRequest();
            xhr.upload.addEventListener('progress', (e) => {
                let progressRate = (e.loaded / e.total) * 100;
                progressCallback(progressRate)
            });
            return xhr;
        }
    })
}