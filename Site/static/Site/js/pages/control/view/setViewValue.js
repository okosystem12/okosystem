import {componentsData} from "../componentsData";
import {userShortName} from "../../../utils/user/userShortName";
import {imgPrep} from "../../../utils/img/imgPrep";
import {controlUserImgList} from "../../../storage/control/controlUserImgList";
import {fileList} from "../../../storage/control/fileList";
import {prepUri} from "../../../utils/file/prepUri";
import {initGallery} from "../../../utils/file/initGallery";
import {info} from "../../../components/card/info";
import {btnToggle} from "./btnToggle";
import {panelFill} from "./panelFill";


export const setViewValue = (data = null) => {
    if (data !== null) {
        let defaultFileList = [];
        const {
            viewModalLabel,
            viewMainPhoto,
            viewPhotoList,
            viewInfo
        } = componentsData;
        viewModalLabel.html(`Карточка ${userShortName(data)}`);

        controlUserImgList.value.filter(el => el.controlUser_id === data.id).forEach(el => {
            const file = fileList.value.find(f => f.id === el.file_id);

            if (file) {
                defaultFileList.push({
                    realId: file.id,
                    name: file.name,
                    url: prepUri(file.file)
                })
            }
        });

        imgPrep(viewMainPhoto, defaultFileList[0]?.url, userShortName(data));

        initGallery(viewPhotoList);
        viewPhotoList.uploaderClean();
        viewPhotoList.uploaderDefaultFiles(defaultFileList);

        viewInfo.html(info(data));

        btnToggle(data);

        panelFill(data);
    }
};