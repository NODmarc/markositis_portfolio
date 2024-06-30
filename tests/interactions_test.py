from locators.interactions_page_locators import InteractionPageLocators as ipl
from pages.interactions_page import InteractionsPage


class TestInteractionsPage:
    class TestSortablePage:
        def test_sortable_list(self, driver):
            sortable_page = InteractionsPage(driver,
                                             'https://demoqa.com/sortable')
            sortable_page.open()
            order_before_list, order_after_list = sortable_page. \
                change_list_order(ipl.TAB_LIST, ipl.LIST_ITEM)
            assert order_before_list != order_after_list, 'The order of the list has not been changed'

        def test_sortable_grid(self, driver):
            sortable_page = InteractionsPage(driver,
                                             'https://demoqa.com/sortable')
            sortable_page.open()
            order_before_grid, order_after_grid = sortable_page. \
                change_list_order(ipl.TAB_GRID, ipl.GRID_ITEM)
            assert order_before_grid != order_after_grid, 'The order of the grid has not been changed'

    class TestSelectable:

        def test_selectable(self, driver):
            selectable_page = InteractionsPage(driver,
                                               'https://demoqa.com/selectable')
            selectable_page.open()
            list_output = selectable_page.select_list_item(
                ipl.SELECTABLE_TAB_LIST,
                ipl.SELECTABLE_LIST_ITEM,
                ipl.SELECTABLE_LIST_ITEM_ACTIVE)
            grid_output = selectable_page.select_list_item(
                ipl.SELECTABLE_TAB_GRID,
                ipl.SELECTABLE_TAB_GRID_ITEM,
                ipl.SELECTABLE_GRID_ITEM_ACTIVE)
            assert len(list_output) > 0, 'No elements were selected'
            assert len(grid_output) > 0, 'No elements were selected'

    class TestResizable:
        def test_resizable(self, driver):
            resizable_page = InteractionsPage(driver,
                                              'https://demoqa.com/resizable')
            resizable_page.open()
            max_size_box, min_size_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            assert max_size_box == (
            '500px', '300px'), 'Max size not equal 500x300'
            assert min_size_box == (
            '150px', '150px'), 'Min size not equal 150x150'
            assert max_resize != min_resize, 'resizable has not been changed'

    class TestDroppable:
        def test_droppable(self, driver):
            droppable_page = InteractionsPage(driver,
                                              'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!', 'No element find or cannot be moved'

        def test_accept(self, driver):
            droppable_page = InteractionsPage(driver,
                                              'https://demoqa.com/droppable')
            droppable_page.open()
            not_acceptable_text, acceptable_text = droppable_page.drop_accept()
            assert not_acceptable_text != 'Dropped!', 'No element find or element is dropped'
            assert acceptable_text == "Dropped!", 'No element find or cannot be moved'

