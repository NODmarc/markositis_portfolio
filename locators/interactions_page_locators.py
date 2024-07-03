from selenium.webdriver.common.by import By


class InteractionPageLocators:
    # sortable page locators
    TAB_LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    LIST_ITEM = (By.CSS_SELECTOR, "div[id='demo-tabpane-list'] div div")
    TAB_GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    GRID_ITEM = (By.CSS_SELECTOR, "div[id='demo-tabpane-grid'] div div div")

    # selectable page locators
    SELECTABLE_TAB_LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    SELECTABLE_LIST_ITEM = (By.CSS_SELECTOR, "ul[id='verticalListContainer'] li")
    SELECTABLE_LIST_ITEM_ACTIVE = (By.CSS_SELECTOR, "ul[id='verticalListContainer'] li[class='mt-2 list-group-item active list-group-item-action']")
    SELECTABLE_TAB_GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    SELECTABLE_TAB_GRID_ITEM = (By.CSS_SELECTOR, "div[id='gridContainer'] li[class='list-group-item list-group-item-action']")
    SELECTABLE_GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, "div[id='gridContainer'] li[class='list-group-item active list-group-item-action']")

    # resizable page locators
    RESIZABLE_BOX = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction']")
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, "div[class='constraint-area'] span[class='react-resizable-handle react-resizable-handle-se']")
    RESIZABLE = (By.CSS_SELECTOR, "div[id='resizable']")
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, "div[id='resizable'] span[class='react-resizable-handle react-resizable-handle-se']")

    # droppable page locators
    SIMPLE_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-simple']")
    SIMPLE_DRAG_ME = (By.CSS_SELECTOR, "div[id='draggable']")
    SIMPLE_DROP_HERE = (By.CSS_SELECTOR, "div[id='simpleDropContainer'] div[id='droppable']")

    ACCEPT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-accept']")
    ACCEPT_DROP_HERE = (By.CSS_SELECTOR, "div[id='acceptDropContainer'] div[id='droppable']")
    ACCEPT_ACCEPTABLE = (By.CSS_SELECTOR, "div[id='acceptable']")
    ACCEPT_NOT_ACCEPTABLE = (By.CSS_SELECTOR, "div[id='notAcceptable']")

    PREVENT_PROPOGATION_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-preventPropogation']")
    PREVENT_PROPOGATION_DRAG_ME = (By.CSS_SELECTOR, "div[id='ppDropContainer'] div[id='dragBox']")
    PREVENT_PROPOGATION_OUTER_DROPPABLE_NOT_GREEDY = (By.CSS_SELECTOR, "div[id='notGreedyDropBox']")
    PREVENT_PROPOGATION_INNER_DROPPABLE_NOT_GREEDY = (By.CSS_SELECTOR, "div[id='notGreedyInnerDropBox']")
    PREVENT_PROPOGATION_OUTER_DROPPABLE_GREEDY = (By.CSS_SELECTOR, "div[id='greedyDropBox']")
    PREVENT_PROPOGATION_INNER_DROPPABLE_GREEDY = (By.CSS_SELECTOR, "div[id='greedyDropBox']")

    REVERT_DRAGGABLE_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-preventPropogation']")
    REVERT_DROP_HERE = (By.CSS_SELECTOR, "div[id='revertableDropContainer'] div[id='droppable']")
    REVERT_WILL_REVERT = (By.CSS_SELECTOR, "div[id='revertable']")
    REVERT_NOT_REVERT = (By.CSS_SELECTOR, "div[id='notRevertable']")

    # draggable page locators
    DRAGGABLE_SIMPLE_TAB = (By.CSS_SELECTOR, "a[id='draggableExample-tab-simple']")
    DRAGGABLE_SIMPLE_DRAG_ME = (By.CSS_SELECTOR, "div[id='dragBox']")

    AXIS_RESTRICTED_TAB = (By.CSS_SELECTOR, "a[id='draggableExample-tab-axisRestriction']")
    AXIS_RESTRICTED_X = (By.CSS_SELECTOR, "div[id='restrictedX']")
    AXIS_RESTRICTED_Y = (By.CSS_SELECTOR, "div[id='restrictedY']")

    CONTAINER_RESTRICTED_TAB = (By.CSS_SELECTOR, "a[id='draggableExample-tab-containerRestriction']")
    CONTAINER_RESTRICTED_CONTAINED_WITH_BOX = (By.CSS_SELECTOR, "#containmentWrapper div")
    CONTAINER_RESTRICTED_CONTAINED_WITH_PARENT = (By.CSS_SELECTOR, '//span[text()="I\'m contained within my parent"]')

    CURSOR_STYLE_TAB = (By.CSS_SELECTOR, "a[id='draggableExample-tab-cursorStyle']")
    CURSOR_STYLE_CENTER = (By.CSS_SELECTOR, "#cursorCenter")
    CURSOR_STYLE_TOP_LEFT = (By.CSS_SELECTOR, "#cursorTopLeft")
    CURSOR_STYLE_BOTTOM = (By.CSS_SELECTOR, "#cursorBottom")


