# Code that automatically copies all issues of a repository to another
from .control_website import login
from .Hardcoded import Hardcoded
from .helper import get_labels_from_issues
from .get_website_controller import get_website_controller
from .get_data import get_issues
from .set_data import set_labels
from .set_data import set_issues
from selenium.webdriver.common.keys import Keys


class Main:
    """ """

    def __init__(self, project_nr, login=True):
        """Initialises object that gets the browser controller, then it gets the issues
        from the source repo, and copies them to the target repo.

        :param project_nr: [Int] that indicates the folder in which this code is stored.
        :param login: [Boolean] True if the website_controller object should be
        created and should login to GitHub.
        """

        # project_nr is an artifact of folder structure
        self.project_nr = project_nr
        self.relative_src_filepath = f"code/project{self.project_nr}/src/"
        # Store the hardcoded values used within this project
        self.hc = Hardcoded()

        # Create a website control object and login to GitHub.
        if login:
            self.website_controller = get_website_controller(self.hc)

            # Get the issues from the source repository.
            issues = get_issues(
                self.hc.source_reponame,
                self.hc.source_username,
                self.website_controller,
            )

            # Filter and set the used labels in the target repo
            used_labels = get_labels_from_issues(issues)
            set_labels(
                used_labels,
                self.hc.target_reponame,
                self.hc.target_username,
                self.website_controller,
            )

            # Add the new issues to the target repo
            set_issues(
                issues,
                self.hc.source_reponame,
                self.hc.source_username,
                self.hc.target_reponame,
                self.hc.target_username,
                self.website_controller,
            )

            # TODO: pass target repository
            # nr_of_issue_pages=self.get_nr_of_issue_pages()


if __name__ == "__main__":
    # initialize main class
    main = Main()