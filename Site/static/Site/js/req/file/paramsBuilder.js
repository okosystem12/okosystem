export const paramsBuilder = (uploaderFile) => {
                let form = new FormData();
                form.append("file", uploaderFile.file);
                return form;
            };