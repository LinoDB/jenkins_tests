import slash
from time import sleep


class RunTests(slash.Test):
    """
    Class that defines the tests to run.
    """


    def before(self) -> None:
        """
        Make tests longer by waiting before every test.
        """

        sleep(1)


    def after(self) -> None:
        """
        Make tests longer by waiting before every test.
        """

        sleep(1)

    
    @slash.repeat(3)
    def test_success(self) -> None:
        """
        Successful test.
        """

        assert 1 == 1
        slash.logger.debug("Ran successful test.")


    @slash.skipped("Failing tests deactivated.")
    def test_failure(self) -> None:
        """
        Failing test.
        """

        slash.logger.debug("This test will fail.")
        assert 1 != 1