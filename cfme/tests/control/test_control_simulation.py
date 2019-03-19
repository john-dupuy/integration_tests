import pytest

from cfme import test_requirements
from cfme.infrastructure.provider import InfraProvider
from cfme.markers.env_markers.provider import ONE_PER_CATEGORY
from cfme.utils.appliance.implementations.ui import navigate_to

pytestmark = [
    pytest.mark.long_running,
    pytest.mark.provider(classes=[InfraProvider], selector=ONE_PER_CATEGORY),
    test_requirements.control,
]


FILL_DATA = {
    "event_type": "Datastore Operation",
    "event_value": "Datastore Analysis Complete",
    "filter_type": "By Clusters",
    "filter_value": "Default",
}


@pytest.mark.tier(1)
def test_control_icons_simulation(appliance, provider):
    """
    Bugzillas:
        * 1349147

    Polarion:
        assignee: jdupuy
        casecomponent: Control
        caseimportance: medium
        initialEstimate: 1/15h
        testSteps:
            1. Have an infrastructure provider
            2. Go to Control -> Simulation
            3. Select:
                Type: Datastore Operation
                Event: Datastore Analysis Complete
                VM Selection: By Clusters, Default
            4. Submit
            5. Check for all icons in this page
        expectedResults:
            1.
            2.
            3.
            4.
            5. All the icons should be present
    """
    view = navigate_to(appliance.server, "ControlSimulation")
    view.fill(FILL_DATA)
    view.submit_button.click()
    # Now check all the icons
    tree = view.simulation_results.tree
    # Check the root_item
    assert tree.image_getter(tree.root_item) is not None
    # Check all the child items
    for child_item in tree.child_items(tree.root_item):
        assert tree.image_getter(child_item) is not None
