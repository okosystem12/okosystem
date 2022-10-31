import {componentsData} from "../../../componentsData";
import {corruptList} from "../../../../../storage/control/corruptList";
import {accordionParent} from "../../../../../components/accordion/accordionParent";
import {accordionPanel} from "../../../../../components/accordion/accordionPanel";
import {link} from "../../../../../components/link";
import {corruptElem} from "../../../../../components/corrupt/corruptElem";
import {corruptParent} from "../../../../../components/corrupt/corruptParent";
import {corruptControl} from "../../../../../components/corrupt/corruptControl";
import {makeBtnEvent} from "./makeBtnEvent";

export const fillAnalysis = (data = null) => {
    console.log('fillAnalysis');
    if (data) {
        const {viewAnalysis} = componentsData;
        viewAnalysis.html('');

        if (corruptList.value.length !== 0) {
            const parent = 'accordionParent';
            const panelList = [];
            const userCorruptList = corruptList.value.filter(el => el.controlUser_id === data.id);

            const socialList = [];

            userCorruptList.forEach(el => {
                const link = el.social[0]['link'];
                if (socialList.indexOf(el.social[0]['link']) === -1) {
                    socialList.push(link);
                }
            });

            socialList.sort().forEach(s => {
                const panelContent = [];

                userCorruptList.forEach(el => {
                    panelContent.push(corruptElem({
                        materialsType: el.materialsType,
                        materials: el.materials,
                        corruptList: el.corruptList
                    }));
                    el.corruptList.forEach(c => {
                        panelContent.push(corruptControl(c))
                    })
                });

                panelList.push(accordionPanel(s, corruptParent(panelContent.join('')), parent))
            });

            viewAnalysis.append(accordionParent(parent, panelList.join('')));

            makeBtnEvent();
        }
    }
};