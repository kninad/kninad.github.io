(require 'ox-publish)
(setq org-publish-project-alist
      '(
        ;; ... add all the components here (see below)...
        ("org-notes"
         :base-directory "~/Desktop/webpage/org/"
         :base-extension "org"
         :publishing-directory "~/Desktop/webpage/public_html/"
         :recursive t
         :publishing-function org-html-publish-to-html
         :headline-levels 4             ; Just the default for this project.
         :auto-preamble t
         )

        ("org-static"
         :base-directory "~/Desktop/webpage/org/"
         :base-extension "css\\|js\\|png\\|jpg\\|gif\\|pdf\\|mp3\\|ogg\\|swf"
         :publishing-directory "~/Desktop/webpage/public_html/"
         :recursive t
         :publishing-function org-publish-attachment
         )

        ("org" :components ("org-notes" "org-static"))
        ))
