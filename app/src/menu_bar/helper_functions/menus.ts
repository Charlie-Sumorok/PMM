import { Menu, MenuItemConstructorOptions } from 'electron';

/** Some menu */
type MainMenu = MenuItemConstructorOptions;

/** Some submenu */
type SubMenu = MainMenu[] | Menu;

export { MainMenu, SubMenu };
