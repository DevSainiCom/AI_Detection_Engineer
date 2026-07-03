"""
Approval Workflow Service
"""


class ApprovalWorkflowService:

    VALID_STATUS = [

        "Draft",

        "AI Generated",

        "Reviewed",

        "Approved",

        "Exported",

    ]

    def update_status(

        self,

        detection,

        status,

    ):

        if status not in self.VALID_STATUS:

            raise ValueError(
                "Invalid status."
            )

        detection["Status"] = status

        return detection


approval_workflow_service = (

    ApprovalWorkflowService()

)