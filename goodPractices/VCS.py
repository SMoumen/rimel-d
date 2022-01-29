from typing import TYPE_CHECKING, Any, Dict, Union

from ansiblelint.rules import AnsibleLintRule

if TYPE_CHECKING:
    from typing import Optional

    from ansiblelint.file_utils import Lintable


class GitHasVersionRule(AnsibleLintRule):
    id = 'git-latest'
    shortdesc = 'Git checkouts must contain explicit version'
    description = (
        'All version control checkouts must point to '
        'an explicit commit or tag, not just ``latest``'
    )
    severity = 'MEDIUM'
    tags = ['idempotency']
    version_added = 'historic'

    def matchtask(
        self, task: Dict[str, Any], file: 'Optional[Lintable]' = None
    ) -> Union[bool, str]:
        return bool(
            task['action']['__ansible_module__'] == 'git'
            and task['action'].get('version', 'HEAD') == 'HEAD'
        )