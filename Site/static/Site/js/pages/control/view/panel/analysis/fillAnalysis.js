import {componentsData} from "../../../componentsData";
import {corruptList} from "../../../../../storage/control/corruptList";
import {accordionParent} from "../../../../../components/accordion/accordionParent";
import {accordionPanel} from "../../../../../components/accordion/accordionPanel";
import {link} from "../../../../../components/link";
import {corruptElem} from "../../../../../components/corrupt/corruptElem";
import {corruptParent} from "../../../../../components/corrupt/corruptParent";
import {corruptControl} from "../../../../../components/corrupt/corruptControl";
import {makeBtnEvent} from "./makeBtnEvent";
import {socialList} from "../../../../../storage/control/socialList";

export const fillAnalysis = (data = null) => {
    if (data) {
        const {viewAnalysis, analysisCount} = componentsData;
        viewAnalysis.html('');
        analysisCount.html(0).hide();

        let count = 0;

        if (corruptList.value.length !== 0) {
            const parent = 'accordionParent';
            const panelList = [];
            const userCorruptList = corruptList.value.filter(el => el.controlUser_id === data.id);

            const sList = [];

            userCorruptList.forEach(el => {
                const link = el.social[0]['link'];
                if (sList.indexOf(el.social[0]['link']) === -1) {
                    sList.push(link);
                }
            });

            sList.sort().forEach(s => {
                const uSocial = socialList.value.find(us => (us.prefix + us.value) === s);
                if(uSocial) {
                    const panelContent = [];
                    let socCount = 0;

                    userCorruptList.filter(el => el.social[0]['link'] === s).forEach(el => {
                        panelContent.push(corruptElem({
                            materialsType: el.materialsType,
                            materials: el.materials,
                            corruptList: el.corruptList
                        }));
                        el.corruptList.forEach(c => {
                            panelContent.push(corruptControl({
                                ...c,
                                type: el.materials.type
                            }));
                            count++;
                            socCount++;
                        })
                    });

                    panelList.push(accordionPanel(s, socCount, corruptParent(panelContent.join('')), parent))
                }
            });

            viewAnalysis.append(accordionParent(parent, panelList.join('')));

            makeBtnEvent();

            if (count) {
                analysisCount.html(count).show();
            }
        }
    }
};