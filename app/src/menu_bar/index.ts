import { Menu } from 'electron';

import { template } from './template';

const menu = Menu.buildFromTemplate(template);
export { menu };
